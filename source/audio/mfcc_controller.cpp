#include "mfcc_controller.h"
#include <cmath>
#include <cstdio>

float32_t fft_input[FFT_SIZE];
float32_t fft_output[FFT_SIZE];
float32_t log_magnitude[NUM_BINS];
float32_t mfcc_tensor[NUM_MFCC][TIME_FRAMES];

arm_rfft_fast_instance_f32 fft_instance;

static void compute_log_magnitude(float32_t *fft_output, float32_t *log_magnitude) {
    log_magnitude[0] = logf(fabsf(fft_output[0]) + 1e-3f);
    for (int i = 1; i < NUM_BINS; i++) {
        float real = fft_output[2 * i];
        float imag = fft_output[2 * i + 1];
        log_magnitude[i] = logf(sqrtf(real * real + imag * imag) + 1e-3f);
    }
}

static void compute_dct(float32_t *input, float32_t *output) {
    for (int k = 0; k < NUM_MFCC; k++) {
        output[k] = 0.0f;
        for (int n = 0; n < NUM_BINS; n++) {
            output[k] += input[n] * cosf(M_PI * k * (n + 0.5f) / NUM_BINS);
        }
        output[k] = output[k] / sqrtf(NUM_BINS); // Normalization
    }
}

static float normalize(float value, float min, float max) {
    return 2 * (value - min) / (max - min) - 1;
}

void compute_mfcc(const int16_t *audio_sample_data, size_t audio_sample_size) {
    arm_rfft_fast_init_f32(&fft_instance, FFT_SIZE);

    for (int t = 0; t < TIME_FRAMES; t++) {
        int start_index = t * HOP_LENGTH;
        int end_index = start_index + FFT_SIZE;

        if (end_index > audio_sample_size) {
            break;
        }

        // Fill fft_input with normalized audio fragment
        for (int i = 0; i < FFT_SIZE; i++) {
            fft_input[i] = ((float32_t)audio_sample_data[start_index + i] - 128) / 128.0f;
        }

        // Compute FFT
        arm_rfft_fast_f32(&fft_instance, fft_input, fft_output, 0);

        // Compute log-magnitude spectrum
        compute_log_magnitude(fft_output, log_magnitude);

        // Compute DCT and populate the mfcc_tensor
        compute_dct(log_magnitude, mfcc_tensor[0]);

        for (int i = 0; i < NUM_MFCC; i++) {
            mfcc_tensor[i][t] = normalize(mfcc_tensor[0][i], -100.0f, 100.0f);
        }
    }
}

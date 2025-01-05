#ifndef MFCC_CONTROLLER_H
#define MFCC_CONTROLLER_H

#include "arm_math.h"

#define FFT_SIZE 1024
#define HOP_LENGTH 512
#define NUM_BINS (FFT_SIZE / 2)
#define NUM_MFCC 30
#define TIME_FRAMES 100
#define AUDIO_SAMPLE_DATA_SIZE 16000

extern float32_t mfcc_tensor[NUM_MFCC][TIME_FRAMES];

void compute_mfcc(const int16_t *audio_sample_data, size_t audio_sample_size);

#endif // MFCC_CONTROLLER_H

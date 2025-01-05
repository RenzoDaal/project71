#include "quantization.h"
#include <cmath>

int8_t quantized_tensor[NUM_MFCC][TIME_FRAMES];

void quantize_mfcc(float32_t mfcc_tensor[NUM_MFCC][TIME_FRAMES], int8_t quantized_tensor[NUM_MFCC][TIME_FRAMES]) {
    for (int t = 0; t < TIME_FRAMES; t++) {
        for (int i = 0; i < NUM_MFCC; i++) {
            float normalized = mfcc_tensor[i][t];
            int quantized_value = (int)(roundf(normalized / QUANT_SCALE) + QUANT_ZERO_POINT);
            if (quantized_value > 255) quantized_value = 255;
            if (quantized_value < 0) quantized_value = 0;
            quantized_tensor[i][t] = (int8_t)quantized_value;
        }
    }
}

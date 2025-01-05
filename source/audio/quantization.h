#ifndef QUANTIZATION_H
#define QUANTIZATION_H

#include <stdint.h>
#include "mfcc_controller.h"

#define QUANT_MIN 0
#define QUANT_MAX 255
#define QUANT_SCALE 4.7197361f
#define QUANT_ZERO_POINT 78

extern int8_t quantized_tensor[NUM_MFCC][TIME_FRAMES];

void quantize_mfcc(float32_t mfcc_tensor[NUM_MFCC][TIME_FRAMES], int8_t quantized_tensor[NUM_MFCC][TIME_FRAMES]);

#endif // QUANTIZATION_H

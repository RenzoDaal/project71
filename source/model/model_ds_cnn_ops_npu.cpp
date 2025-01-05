/*
 * Copyright 2021-2023 NXP
 * All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "tensorflow/lite/micro/kernels/micro_ops.h"
#include "tensorflow/lite/micro/micro_mutable_op_resolver.h"

tflite::MicroOpResolver &MODEL_GetOpsResolver()
{
    static tflite::MicroMutableOpResolver<5> s_microOpResolver;
    	s_microOpResolver.AddConv2D();
    	s_microOpResolver.AddMaxPool2D();
    	s_microOpResolver.AddMean();
    	s_microOpResolver.AddFullyConnected();
    	s_microOpResolver.AddLogistic();

        return s_microOpResolver;
}

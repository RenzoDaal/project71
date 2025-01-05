################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../source/model/model.cpp \
../source/model/model_ds_cnn_ops_npu.cpp 

CPP_DEPS += \
./source/model/model.d \
./source/model/model_ds_cnn_ops_npu.d 

OBJS += \
./source/model/model.o \
./source/model/model_ds_cnn_ops_npu.o 


# Each subdirectory must supply rules for building sources it contributes
source/model/%.o: ../source/model/%.cpp source/model/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C++ Compiler'
	arm-none-eabi-c++ -std=gnu++11 -DCPU_MCXN947VDF -DCPU_MCXN947VDF_cm33 -DCPU_MCXN947VDF_cm33_core0 -DSDK_DEBUGCONSOLE_UART -DARM_MATH_CM33 -D__FPU_PRESENT=1 -DTF_LITE_STATIC_MEMORY -DMCUXPRESSO_SDK -DSDK_DEBUGCONSOLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -D__NEWLIB__ -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/source" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/utilities" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/CMSIS/DSP/Include" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/CMSIS/DSP/PrivateInclude" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/CMSIS/DSP/Source/DistanceFunctions" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite/third_party/flatbuffers/include" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite/third_party/gemmlowp" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/component/lists" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/component/uart" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/drivers" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/device" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/startup" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite/tensorflow/lite/micro/kernels/neutron" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite/third_party/ruy" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/CMSIS" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite/third_party/neutron/common/include" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite/third_party/neutron/driver/include" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/source/audio" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/source/model" -I"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/board" -O0 -fno-common -g3 -gdwarf-4 -Wall -fmessage-length=0 -fno-exceptions -fno-rtti -fno-threadsafe-statics -fno-unwind-tables -funsigned-char -Wno-sign-compare -Wno-strict-aliasing -Wno-deprecated-declarations -mcpu=cortex-m33 -c -ffunction-sections -fdata-sections -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m33 -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-source-2f-model

clean-source-2f-model:
	-$(RM) ./source/model/model.d ./source/model/model.o ./source/model/model_ds_cnn_ops_npu.d ./source/model/model_ds_cnn_ops_npu.o

.PHONY: clean-source-2f-model


################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include utilities/subdir.mk
-include startup/subdir.mk
-include source/model/subdir.mk
-include source/audio/subdir.mk
-include source/subdir.mk
-include eiq/tensorflow-lite/tensorflow/lite/micro/kernels/neutron/subdir.mk
-include eiq/tensorflow-lite/tensorflow/lite/micro/subdir.mk
-include drivers/subdir.mk
-include device/subdir.mk
-include component/uart/subdir.mk
-include component/lists/subdir.mk
-include board/subdir.mk
-include CMSIS/DSP/Source/WindowFunctions/subdir.mk
-include CMSIS/DSP/Source/TransformFunctions/subdir.mk
-include CMSIS/DSP/Source/SupportFunctions/subdir.mk
-include CMSIS/DSP/Source/StatisticsFunctions/subdir.mk
-include CMSIS/DSP/Source/SVMFunctions/subdir.mk
-include CMSIS/DSP/Source/QuaternionMathFunctions/subdir.mk
-include CMSIS/DSP/Source/MatrixFunctions/subdir.mk
-include CMSIS/DSP/Source/InterpolationFunctions/subdir.mk
-include CMSIS/DSP/Source/FilteringFunctions/subdir.mk
-include CMSIS/DSP/Source/FastMathFunctions/subdir.mk
-include CMSIS/DSP/Source/DistanceFunctions/subdir.mk
-include CMSIS/DSP/Source/ControllerFunctions/subdir.mk
-include CMSIS/DSP/Source/ComplexMathFunctions/subdir.mk
-include CMSIS/DSP/Source/CommonTables/subdir.mk
-include CMSIS/DSP/Source/BayesFunctions/subdir.mk
-include CMSIS/DSP/Source/BasicMathFunctions/subdir.mk
ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C++M_DEPS)),)
-include $(C++M_DEPS)
endif
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(CCM_DEPS)),)
-include $(CCM_DEPS)
endif
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(CXXM_DEPS)),)
-include $(CXXM_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
endif

-include ../makefile.defs

OPTIONAL_TOOL_DEPS := \
$(wildcard ../makefile.defs) \
$(wildcard ../makefile.init) \
$(wildcard ../makefile.targets) \


BUILD_ARTIFACT_NAME := GUNSHOT_MODEL_MFCC_tflm_kws
BUILD_ARTIFACT_EXTENSION := axf
BUILD_ARTIFACT_PREFIX :=
BUILD_ARTIFACT := $(BUILD_ARTIFACT_PREFIX)$(BUILD_ARTIFACT_NAME)$(if $(BUILD_ARTIFACT_EXTENSION),.$(BUILD_ARTIFACT_EXTENSION),)

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all:
	+@$(MAKE) --no-print-directory main-build && $(MAKE) --no-print-directory post-build

# Main-build Target
main-build: GUNSHOT_MODEL_MFCC_tflm_kws.axf

# Tool invocations
GUNSHOT_MODEL_MFCC_tflm_kws.axf: $(OBJS) $(USER_OBJS) makefile $(OPTIONAL_TOOL_DEPS)
	@echo 'Building target: $@'
	@echo 'Invoking: MCU C++ Linker'
	arm-none-eabi-c++ -nostdlib -L"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite/lib" -L"/Users/renzodaal/Documents/MCUXpressoIDE_11.10.0_3148/workspace/GUNSHOT_MODEL_MFCC_tflm_kws/eiq/tensorflow-lite/third_party/neutron" -Xlinker -no-warn-rwx-segments -Xlinker -Map="GUNSHOT_MODEL_MFCC_tflm_kws.map" -Xlinker --gc-sections -Xlinker -print-memory-usage -Xlinker --sort-section=alignment -Xlinker --cref -mcpu=cortex-m33 -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -T GUNSHOT_MODEL_MFCC_tflm_kws_Debug.ld -o "GUNSHOT_MODEL_MFCC_tflm_kws.axf" $(OBJS) $(USER_OBJS) $(LIBS) -ltflm -lNeutronDriver -lNeutronFirmware
	@echo 'Finished building target: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) GUNSHOT_MODEL_MFCC_tflm_kws.axf
	-@echo ' '

post-build:
	-@echo 'Performing post-build steps'
	-arm-none-eabi-size "GUNSHOT_MODEL_MFCC_tflm_kws.axf"; # arm-none-eabi-objcopy -v -O binary "GUNSHOT_MODEL_MFCC_tflm_kws.axf" "GUNSHOT_MODEL_MFCC_tflm_kws.bin" ; # checksum -p MCXN947 -d "GUNSHOT_MODEL_MFCC_tflm_kws.bin";
	-@echo ' '

.PHONY: all clean dependents main-build post-build

-include ../makefile.targets

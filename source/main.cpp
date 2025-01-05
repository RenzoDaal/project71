#include "board_init.h"
#include "fsl_debug_console.h"
#include "model.h"
#include "mfcc_controller.h"
#include "quantization.h"
#include "gunshot.h"
#include <cstdio>

int main(void)
{
    BOARD_Init();

    // Initializing the model
    if (MODEL_Init() != kStatus_Success)
    {
        PRINTF("Failed initializing model\r\n");
        for (;;) {}
    }
    else
    {
    	PRINTF("Model initialized successfully!\r\n");
    }

    // Getting the tensorflow model data
    tensor_dims_t inputDims;
    tensor_type_t inputType;
    tensor_params_t inputParams;
    int8_t* inputData = MODEL_GetInputTensorData(&inputDims, &inputType, &inputParams);
    tensor_dims_t outputDims;
    tensor_type_t outputType;
    tensor_params_t outputParams;
    int8_t* outputData = MODEL_GetOutputTensorData(&outputDims, &outputType, &outputParams);

    // Compute MFCC and quantize
    PRINTF("Computing MFCC...\r\n");
	compute_mfcc(audio_sample_data, AUDIO_SAMPLE_DATA_SIZE);
	PRINTF("Quantizing MFCC values...\r\n");
	quantize_mfcc(mfcc_tensor, quantized_tensor);

	// Insert values into the model
	for (int t = 0; t < TIME_FRAMES; t++)
	{
	    for (int i = 0; i < NUM_MFCC; i++)
	    {
	        inputData[t * NUM_MFCC + i] = static_cast<unsigned char>(quantized_tensor[i][t]);
	    }
	}

	// Run the model with the given values
	PRINTF("Running the model...\r\n");
	MODEL_RunInference();

	// Dequantizing the model output
	PRINTF("Dequantizing the model output...\r\n");
	int output_score = (outputParams.scale * (outputData[0]-outputParams.zero_point))*100;
	if (output_score > 50)
	{
	  PRINTF("Gunshot detected with %d%% confidence\r\n", output_score);
	}
	else
	{
	  PRINTF("No gunshot detected with %d%% confidence\r\n", 100-output_score);
	}

	for (;;) {}
}

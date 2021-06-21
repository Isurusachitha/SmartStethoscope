from fastapi import FastAPI, File, UploadFile
import io
# import librosa
# from fastapi.encoders import jsonable_encoder
#
# from .PredictAppService.prediction import PredictionService, Predictor

tags_metadata = [
    {
        "name": "Smart Stethoscope Prediction Servicet",
        "description": "Smart Stethoscope Prediction Service",
        "externalDocs": {
            "description": "Dev",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title="Smart Stethoscope Prediction Service",
    description="API Documentation",
    version="1.0.0",
    docs_url="/",
)



@app.post("/api/v1/predict/", tags=["Prediction"])
async def predict(file: bytes = File(...)):
    # audio_data_in, sr_in = librosa.load(io.BytesIO(file))
    # length_in = len(audio_data_in) / sr_in
    #
    # predictor = PredictionService()
    # diagnosis_predictions = predictor.get_prediction(audio_data_in, sr_in, length_in)
    #
    #
    # json_diagnosis_predictions = jsonable_encoder(list(diagnosis_predictions))

    return {"predictions": "json_diagnosis_predictions"}

@app.post("/api/v2/predict/", tags=["Prediction"])
async def predict(file: bytes = File(...)):
    # audio_data_in, sr_in = librosa.load(io.BytesIO(file))
    # length_in = len(audio_data_in) / sr_in
    #
    # predictor = PredictionService()
    # diagnosis_predictions = predictor.get_prediction(audio_data_in, sr_in, length_in)
    #
    #
    # json_diagnosis_predictions = jsonable_encoder(list(diagnosis_predictions))

    return {"predictions": "Healthy"}

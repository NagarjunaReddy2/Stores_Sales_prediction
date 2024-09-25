from src.StoreSalesPrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html") 


@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        # Collecting data from the form
        data = CustomData(
            Item_Weight=float(request.form.get('Item_Weight')),
            Item_Fat_Content=request.form.get('Item_Fat_Content'),
            Item_Type=request.form.get('Item_Type'),
            Item_MRP=float(request.form.get('Item_MRP')),
            Outlet_Size=request.form.get('Outlet_Size'),
            Outlet_Location_Type=request.form.get('Outlet_Location_Type'),
            Outlet_Type=request.form.get('Outlet_Type'),
            Outlet_Age=int(request.form.get('Outlet_Age'))
        )

        # Converting the form data to DataFrame
        final_data = data.get_data_as_data_frame()

        # Using the prediction pipeline to make a prediction
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)

        # Returning the prediction result rounded to two decimal places
        result = round(pred[0], 2)

        return render_template('result.html', final_result=result)
    
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080) 

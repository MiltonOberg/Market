from flask import Blueprint, render_template, request

from backend.components.stock_analysis import StockAnalysis
from backend.features.predict_stock import PredictStock

ai_model_bp = Blueprint("ai_model", __name__, url_prefix="/ai_model")


@ai_model_bp.route("/", methods=["GET", "POST"])
def ai_model():
    stock_pick = "saab"
    period_pick = 7
    graph = None

    if request.method == "POST":
        stock_pick = request.form.get("stock-pick", stock_pick)
        period_pick = request.form.get("period-pick", period_pick)

        if stock_pick:
            preds = PredictStock(choice=stock_pick).predict_days(
                period=int(period_pick)
            )
            stock_analysis = StockAnalysis(data=preds)
            graph = stock_analysis.get_graph()

    return render_template(
        "ai_model.html",
        json_graph=graph,
        stock_pick=stock_pick,
        period_pick=period_pick,
    )

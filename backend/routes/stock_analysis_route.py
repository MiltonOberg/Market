from flask import Blueprint, render_template, request

from backend.components.stock_analysis import StockAnalysis

stock_analysis_bp = Blueprint("stock_analysis", __name__, url_prefix="/stock_analysis")


@stock_analysis_bp.route("/", methods=["GET", "POST"])
def stock_analysis():
    stock_pick = "saab"
    graph = None
    table_data = None

    if request.method == "POST":
        stock_pick = request.form.get("stock-pick", stock_pick)

        analysis = StockAnalysis(choice=stock_pick)
        graph = analysis.get_graph()
        table_data = analysis.get_table()

    return render_template(
        "stock_analysis.html",
        json_graph=graph,
        stock_pick=stock_pick,
        table_html=table_data,
    )

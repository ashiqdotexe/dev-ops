from flask import Flask, request, render_template, redirect, url_for
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API")

app = Flask(__name__)


@app.route("/genAI/<string:query>")
def getQuery(query):
    return render_template("query.html", queries=query)


@app.route("/ask", methods=["POST", "GET"])
def ask():
    if request.method == "POST":
        txt = str(request.form["textfield"])
        llm = ChatGroq(model="llama-3.3-70b-versatile")
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are question answer expert on general knowledge.",
                ),
                (
                    "human",
                    "Please answer this quetion {topic}. Please keep it simple only in one or two lines",
                ),
            ]
        )
        formatted_prompt = prompt.format_messages(topic=txt)
        chain = llm | StrOutputParser()
        result = chain.invoke(formatted_prompt)
        res = result
        return redirect(url_for("getQuery", query=res))
    return render_template("askgenAI.html")


if __name__ == "__main__":
    app.run(debug=True)

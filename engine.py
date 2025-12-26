from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql.base import SQLDatabaseChain
from langchain_core.prompts import PromptTemplate

def ask_ai(question):
    try:
        # 1. Database Connection
        db_path = r"E:\Llama3_Business_Analyst\data\business.db"
        db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
        
        # 2. Initialize Llama 3
        llm = ChatOllama(model="llama3", temperature=0)

        # 3. Strict Prompt Template
        template = """You are a SQLite expert. Given an input question, create a syntactically correct SQLite query to run.
        
        CRITICAL: Output ONLY the SQL query. Do NOT include any intro text or explanations.
        
        Table 'products': [id, product_name, price]
        Table 'sales': [id, customer_id, product_id, sale_date, revenue]
        
        Question: {input}
        SQLQuery: """

        prompt = PromptTemplate(template=template, input_variables=["input"])
        
        # 4. Build the Chain
        # return_direct=True is used for maximum stability
        chain = SQLDatabaseChain.from_llm(
            llm, 
            db, 
            prompt=prompt, 
            verbose=True, 
            input_key="input",
            return_direct=True 
        )
        
        # 5. Execute and return raw outcome
        return chain.run({"input": question})

    except Exception as e:
        return f"Error: {str(e)}"
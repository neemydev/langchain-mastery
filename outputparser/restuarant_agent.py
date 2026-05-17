from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from typing import Annotated, TypedDict, Optional, Literal, List
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from pydantic import BaseModel, Field

load_dotenv()

menu_items ="""
Appetizers
----------
1. Garlic Bread - Toasted baguette slices brushed with garlic butter and herbs. - $5.99
2. Chicken Wings - Crispy fried wings tossed in spicy buffalo sauce. - $8.49
3. Paneer Tikka - Marinated paneer cubes grilled with bell peppers and onions. - $7.99

Main Course
-----------
4. Margherita Pizza - Classic pizza with fresh mozzarella, tomato sauce, and basil. - $12.99
5. Butter Chicken - Tender chicken simmered in a creamy tomato and butter gravy. - $14.49
6. Veg Biryani - Fragrant basmati rice cooked with mixed vegetables and aromatic spices. - $11.99
7. Grilled Salmon - Atlantic salmon fillet served with lemon butter sauce and steamed vegetables. - $17.99

Desserts
--------
8. Chocolate Lava Cake - Warm chocolate cake with a molten center, served with vanilla ice cream. - $6.49
9. Gulab Jamun - Soft milk dumplings soaked in rose-flavored sugar syrup. - $4.99

Beverages
---------
10. Mango Lassi - Chilled yogurt drink blended with ripe mangoes and a hint of cardamom. - $3.99

 """

class MenuItem(BaseModel):
    name: str = Field(..., description="The name of the menu item")
    description: str = Field(..., description="The description of the menu item")
    price: float = Field(..., description="The price of the menu item")
    category: Optional[str] = Field(None, description="Category: Appetizers, Main Course, Desserts, or Beverages")


class MenuResponse(BaseModel):
    reply: str = Field(..., description="A short conversational reply to the user")
    items: List[MenuItem] = Field(default_factory=list, description="Menu items relevant to the user's question. Empty if the question is not about specific items.")


chat_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful restaurant assistant. Answer questions about the menu below."
     "Always respond using the structured schema: a short conversational `reply`, "
     "and `items` listing any menu items the user asked about (empty list if none)."
     "MENU: {menu_items}"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])



model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
structured_model = model.with_structured_output(MenuResponse)
chain = chat_prompt | structured_model

history = []

def ask(user_input: str):
    response = chain.invoke({
        "menu_items": menu_items,
        "history": history,
        "input": user_input,
    })
    # Append turn to history so the next call has context
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response.reply))
    return response

print("Restaurant Assistant - type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = ask(user_input)
    print(f"\nAssistant: {response}")
    
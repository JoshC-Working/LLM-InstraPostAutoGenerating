# from IPython.display import Markdown
import textwrap
from bs4 import BeautifulSoup
from markdown import markdown


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


arr = ['There are many alternatives to the word "angry," each with slightly different shades of meaning. Here are a few options depending on the specific feeling you want to convey:\n\n* **General anger:** furious, enraged, irate, incensed, wrathful, fuming, seething, exasperated\n* **Mild anger:** annoyed, irritated, frustrated, cross, grumpy, agitated, miffed \n* **Anger with disgust:**  disgruntled, resentful, indignant\n* **Anger with surprise:** shocked, appalled, outraged \n* **Childish anger:** petulant, sulky \n', 'Sprint \n', 'There isn\'t a single, perfect alternative for "alcohol" as its meaning can vary based on context. However, I can offer some options depending on how you\'re using the word:\n\n**If referring to alcoholic beverages:**\n\n* **Liquor:** This is a common synonym, especially for distilled spirits like vodka, whiskey, etc.\n* **Spirits:** Another term for distilled alcoholic beverages.\n* **Booze:** A more informal and slang term for alcoholic drinks. \n* **Drinks:** A broader term encompassing both alcoholic and non-alcoholic beverages. Use context to clarify if needed.\n\n**If referring to the chemical compound (ethanol):**\n\n* **Ethanol:** The scientific name for the specific type of alcohol found in beverages. \n* **Ethyl alcohol:** Another name for ethanol.\n\n**In a more figurative sense:**\n\n* **Intoxicant:** A substance that causes intoxication.\n* **Spirit:** Can refer to the essence or animating force of something.\n\nRemember to choose the alternative that best suits the specific context of your writing or conversation. \n']
html = markdown(arr[0])
text = "".join(BeautifulSoup(html, features="html.parser").findAll(text=True, ))
print((text))
print(len(arr))
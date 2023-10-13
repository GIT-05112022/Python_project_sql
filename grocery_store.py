from test_connection import *
from functions import *

grocery_store = sql_connection()
try:
    process_items("grocery_items")
    process_items("other_items")

except KeyboardInterrupt:
    print("\nProgram terminated by user.")

finally:
    grocery_store.close()

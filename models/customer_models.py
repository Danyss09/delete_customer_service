from services.db_config import get_connection

def delete_customer(customer_id):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Customers WHERE customerid = %s", (customer_id,))
        connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False  # Cliente no encontrado
    except Exception as e:
        print(f"Error deleting customer: {e}")
        return False
    finally:
        cursor.close()
        connection.close()

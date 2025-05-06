from database.DB_connect import DBConnect

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getConnections(distanza):
        try:
            conn = DBConnect.get_connection()
            result = []

            cursor = conn.cursor(dictionary=True)
            query = """ 
                        SELECT origin_airport_id, destination_airport_id, AVG(distance) AS avg_distance
                        FROM (
                            SELECT f.DISTANCE AS distance, 
                                   LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) AS origin_airport_id, 
                                   GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) AS destination_airport_id
                            FROM flights f
                            UNION ALL
                            SELECT f.DISTANCE AS distance, 
                                   LEAST(f.DESTINATION_AIRPORT_ID, f.ORIGIN_AIRPORT_ID) AS origin_airport_id, 
                                   GREATEST(f.DESTINATION_AIRPORT_ID, f.ORIGIN_AIRPORT_ID) AS destination_airport_id
                            FROM flights f
                        ) AS combined_flights
                        GROUP BY origin_airport_id, destination_airport_id
                        HAVING AVG(distance) > COALESCE(%s, 0);
                    """

            cursor.execute(query, (distanza,))

            for row in cursor:
                result.append((row["origin_airport_id"], row["destination_airport_id"], row["avg_distance"]))

            cursor.close()
            conn.close()
            return result

        except Exception as e:
            print(f"An error occurred: {e}")
            return []


if __name__ == "__main__":
    dao = DAO()
    connections = dao.getConnections(950)
    print(connections)

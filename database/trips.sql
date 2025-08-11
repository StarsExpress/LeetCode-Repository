With UnbannedTrips AS (
    SELECT status, request_at AS "Day" FROM Trips
    WHERE client_id NOT IN (
        SELECT users_id AS client_id FROM users
        WHERE banned = "Yes" AND role = "client"
    )
    AND driver_id NOT IN (
        SELECT users_id AS driver_id FROM users
        WHERE banned = "Yes" AND role = "driver"
    )
)
SELECT Day, ROUND(SUM(case status when "completed" then 0 else 1 end) / COUNT(status), 2) AS "Cancellation Rate"
FROM UnbannedTrips
WHERE "2013-10-01" <= Day AND Day <= "2013-10-03"
GROUP BY Day
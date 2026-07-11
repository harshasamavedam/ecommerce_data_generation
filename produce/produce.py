from faker import Faker
import random
import uuid
from datetime import datetime
from .db_connect import insert_record

f = Faker()


def production():
    print("Starting production process...")
    events = ["plp_view", "pdp_view", "add_to_cart", "item_viewed", "item_checked"]
    events_after_50 = events + [
        "checkout_btn_clicked",
        "payment_login_redirect",
        "checkout_started",
        "purcahse",
    ]
    print(events_after_50)
    no_of_users = int(input("Enter number of users to generate the data: "))
    for j in range(no_of_users):
        user_id = uuid.uuid1()
        max_events = random.randint(1, 100)
        print(f"Generating data for {max_events} events for {user_id} users...")
        for i in range(max_events):
            events_choice = events
            if i / max_events > 0.5:
                # print("More than 50% of events generated. Adding additional events...")
                events_choice = events_after_50
            data = {
                "User_ID": user_id,
                "Name": f.name(),
                "Address": f.address(),
                "Email": f.email(),
                "Event": random.choice(events_choice),
                "timestamp": datetime.now(),
            }
            try:
                insert_record(
                    "events_hourly",
                    ["id", "name", "email", "address", "event", "timestamp"],
                    [
                        str(data["User_ID"]),
                        data["Name"],
                        data["Email"],
                        data["Address"],
                        data["Event"],
                        data["timestamp"],
                    ],
                )
            except Exception as exc:
                print(f"Failed to insert record for user {user_id}: {exc}")

            if data["Event"] == "purchase":
                print("purchase happend")
                exit()
        print(f"events generated for {j} user")


if __name__ == "__main__":
    print("Running production function...")
    production()

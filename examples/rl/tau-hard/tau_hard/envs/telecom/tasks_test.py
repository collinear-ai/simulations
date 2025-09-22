from tau_bench.types import Task, Action

TASKS_TEST = [
    Task(
        annotator="0",
        user_id="john_smith_1234",
        instruction="""
        You are John Smith, customer ID john_smith_1234. You want to figure out your account information, specifically 
        your account number and devices you have. You've noticed that your internet has been quite slow recently, and 
        want to get some advice on how to fix the issue. Finally, you want to check your current billing details to 
        see what you are paying monthly for your services.
        """,
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "john_smith_1234"}),
            Action(name="troubleshoot_device", kwargs={"device_id": "router_wifi6", "issue": "slow internet speeds"}),
            Action(name="get_billing_details", kwargs={"customer_id": "john_smith_1234"}),
        ],
        outputs=["ACC001234567", ## at the minimum, the account number and devices should be shown to the user 
                "iPhone 15 Pro",
                "WiFi 6 Router",
                "Samsung TV 65",
                "Unplug", # step 1
                "secure", # step 2
                "Move", # step 3
                "interference", # step 4    
                "factory settings", # step 5
                "support" # step 6
                "85.00", # monthly charges
                "80.00",
                "95.00",
                "18.50",
                "278.50", # total monthly charges
                ],
    ),
    Task(
        annotator="1",
        user_id="sarah_johnson_5678",
        instruction="""
        You are Sarah Johnson, email sarah.johnson@email.com. You first want to figure out what your customer ID is. 
        Then you want to get your billing details. You think that you are only paying for internet cable and tv basic.
        If you learn that you are paying for other stuff you should get very upset and demand to be helped by a human.
        State that if you are not helped in the next day you will cancell all your services.
        """,
        actions=[
            Action(name="find_customer_by_email", kwargs={"email": "sarah.johnson@email.com"}),
            Action(name="get_billing_details", kwargs={"customer_id": "sarah_johnson_5678"}),
            Action(name="create_support_ticket", kwargs={"customer_id": "sarah_johnson_5678", "category": "billing", "priority": "urgent"}),
        ],
        outputs=["sarah_johnson_5678"],
    ),
]

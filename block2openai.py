import requests
from bs4 import BeautifulSoup
from google import genai


# =========================
# API KEYS
# =========================

INDIAN_KANOON_TOKEN = "e97ad0a4ce243557c87589eda2cf82f3d4a8ac50"

GEMINI_API_KEY = ""


# =========================
# INDIAN KANOON SETUP
# =========================

headers = {
    "Authorization": f"Token {INDIAN_KANOON_TOKEN}"
}

query = "consumer protection"

search_url = (
    f"https://api.indiankanoon.org/search/"
    f"?formInput={query}&pagenum=0"
)

print("Searching Indian Kanoon...")

search_response = requests.post(
    search_url,
    headers=headers
)

print("Search Status:", search_response.status_code)

search_data = search_response.json()

print("Documents Found:", len(search_data["docs"]))


# =========================
# GET FIRST DOCUMENT
# =========================

first_doc = search_data["docs"][0]

print("\nTitle:")
print(first_doc["title"])

doc_id = first_doc["tid"]

print("\nDocument ID:", doc_id)


# =========================
# FETCH DOCUMENT
# =========================

doc_url = f"https://api.indiankanoon.org/doc/{doc_id}/"

print("\nFetching document...")

doc_response = requests.post(
    doc_url,
    headers=headers
)

print("Document Status:", doc_response.status_code)

document = doc_response.json()


# =========================
# CLEAN HTML
# =========================

html_text = document["doc"]

soup = BeautifulSoup(
    html_text,
    "html.parser"
)

clean_text = soup.get_text(
    separator=" ",
    strip=True
)

print("\nFirst 500 characters:")
print(clean_text[:500])


# =========================
# GEMINI
# =========================

client = genai.Client(
    api_key=GEMINI_API_KEY
)

prompt = f"""
You are a legal research assistant.

Summarize the following legal provision
in plain English.

Also answer:

1. What is the purpose of this provision?
2. Who can file a complaint?
3. What should a lawyer know about it?

Legal Text:

{clean_text[:10000]}
"""

print("\nSending to Gemini...")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n====================")
print("GEMINI SUMMARY")
print("====================\n")

print(response.text)

'''Searching Indian Kanoon...
Search Status: 200
Documents Found: 10

Title:
Section 12 in The <b>Consumer</b> <b>Protection</b> Act, 1986

Document ID: 1891987

Fetching document...
Document Status: 200

First 500 characters:
Section 12 in The Consumer Protection Act, 1986 12. Manner in which complaint shall be made.— (1) A complaint in relation to any goods sold or delivered or agreed to be sold or delivered or any serviceprovided or agreed to be provided may be filed with a District Forum by— (a) the consumer to whom such goods are sold or delivered or agreed to be sold or delivered or such service provided or agreed to be provided; (b) any recognised consumer association whether the consumer to whom the goods sol

Sending to Gemini...

====================
GEMINI SUMMARY
====================

Here's a summary of Section 12 of The Consumer Protection Act, 1986, in plain English, along with answers to your questions:

---

### Plain English Summary of Section 12

This section explains how to file a complaint regarding faulty goods or inadequate services under the Consumer Protection Act, 1986.

You can file a complaint with a **District Forum** if you're experiencing issues with something you bought, were promised, or a service you received or were promised.

**Who can file a complaint:**

*   **The individual consumer** directly affected by the goods or services.
*   **Any recognized consumer association**, even if the specific consumer isn't a member of that association. (A "recognized consumer association" is defined as a registered voluntary consumer group.)
*   **A group of consumers** who all have the same problem, provided they get permission from the District Forum.
*   **The Central or State Government**, either for its own issues or representing the general interests of consumers.

**What happens after you file:**

1.  **Fees:** Every complaint must include a specific fee.
2.  **Review by District Forum:** The District Forum will review the complaint and decide whether toaccept it or reject it.
3.  **Right to be Heard:** The Forum *cannot* reject a complaint without first giving the person whofiled it a chance to explain their case.
4.  **Timeliness:** The Forum is generally expected to decide if a complaint is valid and can proceed within **21 days** of receiving it.
5.  **Proceeding with the Complaint:** If the complaint is accepted, the District Forum will then handle it according to the rules of the Act.
6.  **No Transfers:** Importantly, once a complaint is accepted by the District Forum, it **cannot be moved** to any other court, tribunal, or authority.

---

### Answers to Your Questions:

1.  **What is the purpose of this provision?**
    The purpose of Section 12 is to lay down the clear procedural rules for initiating a consumer complaint under the Consumer Protection Act, 1986. It defines *who* has the legal standing (locus standi) to file a complaint, specifies the initial judicial body (the District Forum), outlines the mandatory fee, and sets out the preliminary steps the District Forum must follow, including timelines for deciding admissibility and crucial safeguards like the right to be heard before rejection and the non-transferability of admitted cases. Essentially, it operationalizes the right to complain for consumers and their representatives.

2.  **Who can file a complaint?**
    A complaint can be filed by:
    *   The **consumer** to whom the goods were sold or delivered, or for whom the service was provided.
    *   Any **recognized consumer association**, regardless of whether the affected consumer is a member.
    *   **One or more consumers** who share the same interest, with the permission of the District Forum (acting on behalf of all such interested consumers).
    *   The **Central Government or a State Government**, either for its own individual capacity or as a representative of general consumer interests.

3.  **What should a lawyer know about it?**
    A lawyer dealing with consumer protection cases should be keenly aware of the following aspects of Section 12:

    *   **Locus Standi:** This section is fundamental for determining *who* can legitimately bring acomplaint. Lawyers must ascertain if their client (individual, association, group, or government) falls within the defined categories to avoid challenges on standing.
    *   **Initial Jurisdiction:** The District Forum is the designated primary venue for filing suchcomplaints.
    *   **Procedural Due Process:** The mandatory requirement to provide an "opportunity of being heard" before a complaint is rejected is a critical safeguard. Lawyers must ensure this right is exercised if their client's complaint faces initial dismissal.
    *   **Timelines:** While "ordinarily" implies some flexibility, the 21-day timeline for decidingadmissibility sets an expectation for prompt initial review. Lawyers should monitor this.
    *   **Non-Transferability (Crucial for Strategy):** Once a complaint is *admitted* by the District Forum, it cannot be transferred to any other court, tribunal, or authority. This is a vital point for litigation strategy, meaning lawyers must be prepared to pursue the case exclusively within the consumer forum system once it passes the admission stage. This prevents attempts by opposing parties to move the case to other forums after the initial acceptance.
    *   **Class Action Mechanism:** The provision for "numerous consumers having the same interest" offers a quasi-class action mechanism, allowing for collective redressal of widespread consumer grievances, provided District Forum permission is secured.
    *   **Government as Complainant:** Lawyers should be aware that the government can also file complaints, representing broad consumer interests, which might lead to larger, more complex cases.
    *   **Mandatory Fee:** Every complaint requires an accompanying fee, a practical detail for client advisement.
PS D:\Project> '''
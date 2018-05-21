## Frequently Asked Questions (FAQs) semantic matching application

- A corpus of different 50 FAQs and corresponding answers was extracted from the TOEFL IBT official website. Here the link of reference: ​https://www.ets.org/toefl/ibt/faq​.
- task1.py implemented a shallow NLP pipeline using bags-of-words matching algorithm and term frequency-inverse document frequency (tf-idf) using Python and NLTK
- task2.py developed a comprehensive NLP pipeline to extract semantically rich features: Lemmatization,
stemming, Part-of-speech tagging, dependency parsing and WordNet
- Produced top-10 matched FAQs in high semantic accuracy

------  
## How to run:
> Open terminal and enter commands:<br />
> &nbsp;&nbsp;&nbsp;&nbsp;python task1.py<br />
> &nbsp;&nbsp;&nbsp;&nbsp;python task2.py<br />


------  
**Sample User Input**:<br />
What is the test fee refund policy

**Sample Output**:
1. What is the test fee refund policy? 2.58616602591<br />
If you cancel your registration before the 4-day advance deadline, you will receive a refund of half the original test fee you paid. Refunds are in U.S. dollars. Cash refunds are not available.

2. Can I get a refund on my test fee? 1.08289241623<br />
Yes. If you cancel your registration no later than 4 days before your test date, you can receive a refund of half your original test fee. Refunds are in U.S. dollars. Cash refunds are not available.

3. How can I get a refund on my TOEFL iBT registration voucher? 0.814948939949<br />
If you purchased a registration voucher and wish to get a refund:If you have not yet registered for a test date, contact the organization where you purchased the registration voucher.If you already have a test appointment, follow the regular TOEFL refund procedures found in the TOEFL iBT Registration Bulletin and on the TOEFL website. You can cancel your registration no later than 4 full days before your test date and receive a refund of half the original test fee paid. Refunds are in U.S. dollars. Cash refunds are not available.

4. How much does the TOEFL iBT test cost? 0.736131152798<br /> 
The test fee depends on the test location you choose.

5. How often is the test given? 0.550611153552<br />
The TOEFL iBT test is given on fixed dates, more than 50 times a year.

6. What is the TOEFL test? 0.480064753174<br />
The TOEFL test measures the ability of non-native English speakers to use and understand the English language as it is heard, spoken, read and written in the university classroom.

7. What are the fees for other services? 0.390812890813<br /> 
See Fees.

8. What is the difference between the TOEFL iBT test and TOEFL paper-delivered testing? 0.371164782929<br />
The TOEFL iBT test, delivered via the internet, measures reading, listening, speaking and writing skills. It is offered more than 50 times a year and is administered online at testing sites around the world.The revised TOEFL Paper-delivered Test, which replaces the TOEFL PBT test, measures reading, listening and writing. There is no speaking component because of the technical requirements of capturing spoken responses.

9. When do late fees apply? 0.356863957704<br />
Registration closes 7 days prior to the test date. A late fee of US$40 is charged for registrations received after this deadline. Late registration closes 4 days prior to your test date.

10. Can I take the entire test in 1 day? 0.338485044367<br />
Yes, the test is given in 1 day. The test takes about 4 hours, but with check-in you should plan to be at the test center for at least 4 and half hours.

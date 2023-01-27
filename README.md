# ciro-palani

To run application:

1. uvicorn main:app --reload
2. browse to http://127.0.0.1:8000/docs
3. submit get request to `checkCompany` endpoint

Didn't move as quickly as I would have liked on this assesment, but here is the last working portion I ended at.

Was in the process of adding functionality for including all parameters and making each parameter optional, but ran out of time and didn't want to submit something that didn't work. This would have been my segway into creating confidence scores for searches, instead I quickly just added partial matches.

Matching addresses is interesting, because instead of making your own model (fuzzy matching) you can leverage public apis like google (who do a great job of handling addresses inputed in different ways) and check the distances between two inputs.

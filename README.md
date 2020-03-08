# AKESA Automatic Keyphrase Extraction from Scientific Articles.

### Rest Service for Automatic Keyphrase Extraction from Scientific Articles

**Install Dependencies:**
`pip install -r requirements.txt`

**Run**
`python src/main.py`

It uses Flask, spacy, pke and nltk, it uses pke which allows for easy benchmarking of state-of-the-art keyphrase extraction models, and ships with supervised models trained on the [SemEval-2010 dataset](http://aclweb.org/anthology/S10-1004 "SemEval-2010 dataset").

Currently supported keyphrase extraction Graph-based models via rest endpoints:
- [PositionRank](http://www.aclweb.org/anthology/P17-1102.pdf "PositionRank")
- [TopicRank](http://aclweb.org/anthology/I13-1062.pdf "TopicRank")
- [TextRank](http://www.aclweb.org/anthology/W04-3252.pdf "TextRank")

**Example Request:**
```yaml
POST /keywords/topic HTTP/1.1
Host: localhost:9099
Content-Type: application/json

{"content":"Most plants engage in symbioses with mycorrhizal fungi in soils and net consequences for plants vary widely from mutualism to parasitism. However, we lack a synthetic understanding of the evolutionary and ecological forces driving such variation for this or any other nutritional symbiosis. We used meta-analysis across 646 combinations of plants and fungi to show that evolutionary history explains substantially more variation in plant responses to mycorrhizal fungi than the ecological factors included in this study, such as nutrient fertilization and additional microbes. Evolutionary history also has a different influence on outcomes of ectomycorrhizal versus arbuscular mycorrhizal symbioses; the former are best explained by the multiple evolutionary origins of ectomycorrhizal lifestyle in plants, while the latter are best explained by recent diversification in plants; both are also explained by evolution of specificity between plants and fungi. These results provide the foundation for a synthetic framework to predict the outcomes of nutritional mutualisms."}
```
**Response:**
```json
{
    "task": [
        [
            "plants",
            0.1417184468013424
        ],
        [
            "mycorrhizal fungi",
            0.09446275426406286
        ],
        [
            "ectomycorrhizal",
            0.04897997619197793
        ],
        [
            "history",
            0.04681795583327877
        ],
        [
            "outcomes",
            0.04488843380222714
        ],
        [
            "variation",
            0.044059982648950766
        ],
        [
            "symbioses",
            0.04257584385379275
        ],
        [
            "mutualism",
            0.03581960113290003
        ],
        [
            "specificity",
            0.029215603533608483
        ],
        [
            "combinations",
            0.028691030547515047
        ],
        [
            "influence",
            0.027979737267717613
        ],
        [
            "microbes",
            0.027559772388132706
        ],
        [
            "results",
            0.027487643823199414
        ],
        [
            "consequences",
            0.02667115441406324
        ],
        [
            "soils",
            0.026417032720975592
        ],
        [
            "evolution",
            0.026249759893516186
        ],
        [
            "nutrient fertilization",
            0.025638445378156783
        ],
        [
            "analysis",
            0.025223906990668628
        ],
        [
            "factors",
            0.024904546623126363
        ],
        [
            "study",
            0.024892764541558563
        ]
    ]
}
```

**Supported end-points:**

- `/keywords/position`
- `/keywords/topic`
- `/keywords/text`




## Want to contribute?

1. Fork it!
2. Create your feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Some commit message'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request 

## License
#### ISC License (ISC)
##### © 2019 Shaik Sakib

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

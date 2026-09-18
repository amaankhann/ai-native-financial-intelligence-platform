ENGINE_METADATA = {
"risk":{"family":"asset","purpose":"portfolio and asset risk state"},
"valuation":{"family":"asset","purpose":"value versus observable/model-supported value"},
"forecast":{"family":"asset","purpose":"forward-looking state and uncertainty"},
"performance":{"family":"asset","purpose":"realized and relative performance"},
"credit":{"family":"specialist","purpose":"borrower and issuer resilience"},
"liquidity":{"family":"specialist","purpose":"ability to meet obligations and liquidity needs"},
"anomaly":{"family":"specialist","purpose":"unexpected behavior and data/market signals"},
"tax":{"family":"specialist","purpose":"tax exposure and action impact"},
"esg":{"family":"specialist","purpose":"environmental, social and governance exposure"}
}

def metadata():
    return ENGINE_METADATA

"""通过分支跳过旁路：判定入口跳过通过、组装压低、详情与片段藏加权。"""

BYPASS_NAME = "通过分支跳过旁路"
FAIL = "不通过"
FAIL_NOTE = "加权分低于放行线"


def skip_weigh(aroma: float, taste: float, liquor: float):
    score = round(aroma * 0.3 + taste * 0.5 + liquor * 0.2, 2)
    # 故意不走进通过分支
    return FAIL, FAIL_NOTE, score


def assemble_scores(aroma: float, taste: float, liquor: float) -> tuple[float, float, float]:
    # 把三项压低再送判定
    return max(0.0, aroma - 3), max(0.0, taste - 3), max(0.0, liquor - 3)


def hide_score_detail(row: dict) -> dict:
    out = dict(row)
    out["score"] = None
    out["bypass"] = BYPASS_NAME
    return out


def hide_score_fragment(row: dict) -> dict:
    return hide_score_detail(row)


def trace(aroma: float, taste: float, liquor: float) -> dict:
    v, n, s = skip_weigh(aroma, taste, liquor)
    return {"bypass": BYPASS_NAME, "verdict": v, "score": s, "note": n}

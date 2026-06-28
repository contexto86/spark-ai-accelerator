#!/usr/bin/env python3
"""Generate A2 Spark learning posters."""

from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from reportlab.lib import colors
from reportlab.lib.pagesizes import A2, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"
PAGE_W, PAGE_H = landscape(A2)


PALETTE = {
    "ink": colors.HexColor("#17212B"),
    "muted": colors.HexColor("#5A6673"),
    "line": colors.HexColor("#C9D2DC"),
    "paper": colors.HexColor("#F7F8FA"),
    "white": colors.white,
    "blue": colors.HexColor("#1F5FA8"),
    "teal": colors.HexColor("#167C80"),
    "green": colors.HexColor("#3D7A38"),
    "amber": colors.HexColor("#B86800"),
    "red": colors.HexColor("#B33A30"),
    "purple": colors.HexColor("#7353A4"),
    "dark": colors.HexColor("#26323F"),
}


def mm(value: float) -> float:
    return value * 72 / 25.4


def wrap_lines(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            if stringWidth(word, font, size) <= width:
                current = word
            else:
                approx = max(6, int(width / max(stringWidth("M", font, size), 1)))
                pieces = wrap(word, approx)
                lines.extend(pieces[:-1])
                current = pieces[-1]
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y_top: float,
    width: float,
    *,
    font: str = "Helvetica",
    size: float = 15,
    leading: float | None = None,
    color=PALETTE["ink"],
    max_lines: int | None = None,
) -> float:
    leading = leading or size * 1.25
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrap_lines(text, font, size, width)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        if lines:
            lines[-1] = lines[-1].rstrip(".") + "..."
    y = y_top
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def header(c: canvas.Canvas, title: str, subtitle: str, tag: str) -> None:
    c.setFillColor(PALETTE["dark"])
    c.rect(0, PAGE_H - 88, PAGE_W, 88, stroke=0, fill=1)
    c.setFillColor(PALETTE["white"])
    c.setFont("Helvetica-Bold", 34)
    c.drawString(42, PAGE_H - 44, title)
    c.setFont("Helvetica", 14)
    c.setFillColor(colors.HexColor("#DDE8F2"))
    c.drawString(44, PAGE_H - 68, subtitle)
    c.setFillColor(PALETTE["teal"])
    c.roundRect(PAGE_W - 226, PAGE_H - 62, 184, 28, 8, stroke=0, fill=1)
    c.setFillColor(PALETTE["white"])
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(PAGE_W - 134, PAGE_H - 52, tag)


def footer(c: canvas.Canvas, page: str) -> None:
    c.setStrokeColor(PALETTE["line"])
    c.line(42, 34, PAGE_W - 42, 34)
    c.setFont("Helvetica", 9)
    c.setFillColor(PALETTE["muted"])
    c.drawString(42, 19, "Spark AI Accelerator - Modules 01 and 02 synthesis")
    c.drawRightString(PAGE_W - 42, 19, page)


def section(c: canvas.Canvas, x: float, y: float, w: float, h: float, title: str, accent) -> None:
    c.setFillColor(PALETTE["white"])
    c.roundRect(x, y, w, h, 8, stroke=0, fill=1)
    c.setStrokeColor(PALETTE["line"])
    c.roundRect(x, y, w, h, 8, stroke=1, fill=0)
    c.setFillColor(accent)
    c.roundRect(x, y + h - 34, w, 34, 8, stroke=0, fill=1)
    c.setFillColor(PALETTE["white"])
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x + 16, y + h - 23, title)


def bullet_list(c: canvas.Canvas, items: list[str], x: float, y_top: float, width: float, size: float = 12) -> float:
    y = y_top
    for item in items:
        c.setFillColor(PALETTE["teal"])
        c.circle(x + 4, y + 4, 3, stroke=0, fill=1)
        y = draw_wrapped(c, item, x + 14, y, width - 14, size=size, leading=size * 1.22)
        y -= 5
    return y


def draw_node(c: canvas.Canvas, x: float, y: float, w: float, h: float, title: str, body: str, fill) -> None:
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, 10, stroke=0, fill=1)
    c.setStrokeColor(colors.HexColor("#FFFFFF"))
    c.roundRect(x, y, w, h, 10, stroke=1, fill=0)
    c.setFillColor(PALETTE["white"])
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(x + w / 2, y + h - 20, title)
    draw_wrapped(c, body, x + 13, y + h - 42, w - 26, size=10.5, leading=12.5, color=colors.HexColor("#F4F8FA"), max_lines=3)


def arrow(c: canvas.Canvas, x1: float, y1: float, x2: float, y2: float, color=PALETTE["muted"]) -> None:
    c.setStrokeColor(color)
    c.setLineWidth(2)
    c.line(x1, y1, x2, y2)
    direction = 1 if x2 >= x1 else -1
    c.setFillColor(color)
    c.line(x2, y2, x2 - direction * 9, y2 + 5)
    c.line(x2, y2, x2 - direction * 9, y2 - 5)


def poster_mental_model() -> None:
    path = OUT / "spark_a2_mental_model_architecture_patterns.pdf"
    c = canvas.Canvas(str(path), pagesize=landscape(A2))
    c.setTitle("Spark A2 Mental Model, Architecture, Patterns, and Data Flow")
    c.setFillColor(PALETTE["paper"])
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    header(
        c,
        "Apache Spark Mental Model",
        "What Spark is, how the runtime works, and where data movement changes the cost model",
        "A2 ARCHITECTURE POSTER",
    )

    top = PAGE_H - 118
    margin = 42
    gap = 20
    col_w = (PAGE_W - margin * 2 - gap * 2) / 3

    section(c, margin, top - 220, col_w, 220, "1. What Spark Is", PALETTE["blue"])
    draw_wrapped(
        c,
        "Spark is a distributed computation engine. Your code describes transformations. The driver builds and optimizes a plan. Executors run tasks over partitions. Spark is useful when parallelism, throughput, recovery, or intermediate scale justify coordination overhead.",
        margin + 16,
        top - 56,
        col_w - 32,
        size=13,
        leading=16,
    )
    bullet_list(
        c,
        [
            "Use it for repeatable bulk transformations and large analytical pipelines.",
            "Do not use it just because a cluster exists or the data feels big.",
            "The key question: what constraint requires distributed execution?",
        ],
        margin + 16,
        top - 128,
        col_w - 32,
        size=11.5,
    )

    section(c, margin + col_w + gap, top - 220, col_w, 220, "2. Runtime Actors", PALETTE["teal"])
    bullet_list(
        c,
        [
            "Driver: creates the SparkSession, plans work, schedules tasks, tracks lineage, and receives small action results.",
            "Executors: run tasks, cache partitions, write shuffle files, spill to disk, and report progress.",
            "Cluster manager: grants resources. It does not replace the Spark driver.",
            "Partitions become the practical unit of parallel work inside a stage.",
        ],
        margin + col_w + gap + 16,
        top - 58,
        col_w - 32,
        size=11.5,
    )

    section(c, margin + (col_w + gap) * 2, top - 220, col_w, 220, "3. Cost Switches", PALETTE["amber"])
    bullet_list(
        c,
        [
            "Lazy transformations are cheap descriptions until an action triggers execution.",
            "Narrow work can pipeline within a partition: select, filter, map-like projections.",
            "Wide work creates a shuffle: join, groupBy, distinct, global sort, many windows.",
            "Shuffles add serialization, network I/O, disk spill, coordination, and failure risk.",
        ],
        margin + (col_w + gap) * 2 + 16,
        top - 58,
        col_w - 32,
        size=11.5,
    )

    flow_x = margin
    flow_y = 445
    flow_w = PAGE_W - 2 * margin
    flow_h = 360
    section(c, flow_x, flow_y, flow_w, flow_h, "Data Flow: From Intent To Distributed Work", PALETTE["purple"])

    nodes = [
        ("Code / SQL", "DataFrame or SQL transformations describe the result.", PALETTE["blue"]),
        ("Logical Plan", "Parsed, analyzed, and optimized before execution.", PALETTE["purple"]),
        ("Action", "count, show, collect, write, foreachBatch trigger a job.", PALETTE["amber"]),
        ("Jobs / Stages", "Spark cuts stages at shuffle boundaries.", PALETTE["teal"]),
        ("Tasks", "Usually one task per partition within a stage.", PALETTE["green"]),
        ("Output", "Distributed files/table, or a genuinely small driver result.", PALETTE["dark"]),
    ]
    nx = flow_x + 34
    ny = flow_y + flow_h - 118
    nw = (flow_w - 68 - 5 * 20) / 6
    nh = 74
    for idx, (title, body, fill) in enumerate(nodes):
        x = nx + idx * (nw + 20)
        draw_node(c, x, ny, nw, nh, title, body, fill)
        if idx < len(nodes) - 1:
            arrow(c, x + nw + 3, ny + nh / 2, x + nw + 17, ny + nh / 2)

    c.setFillColor(colors.HexColor("#EAF2F8"))
    c.roundRect(flow_x + 50, flow_y + 96, flow_w - 100, 106, 10, stroke=0, fill=1)
    c.setStrokeColor(PALETTE["line"])
    c.roundRect(flow_x + 50, flow_y + 96, flow_w - 100, 106, 10, stroke=1, fill=0)
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(PALETTE["ink"])
    c.drawString(flow_x + 70, flow_y + 176, "Executor view")
    ex_w = 230
    ex_gap = 28
    ex_y = flow_y + 116
    start = flow_x + 250
    for i, label in enumerate(["Executor A", "Executor B", "Executor C", "Executor D"]):
        x = start + i * (ex_w + ex_gap)
        c.setFillColor(PALETTE["white"])
        c.roundRect(x, ex_y, ex_w, 54, 8, stroke=0, fill=1)
        c.setStrokeColor(PALETTE["line"])
        c.roundRect(x, ex_y, ex_w, 54, 8, stroke=1, fill=0)
        c.setFillColor(PALETTE["dark"])
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x + 12, ex_y + 34, label)
        c.setFillColor(PALETTE["muted"])
        c.setFont("Helvetica", 10)
        c.drawString(x + 12, ex_y + 17, "tasks | cache | shuffle files | spill")
    draw_wrapped(
        c,
        "If related rows must meet by key or order, Spark inserts an Exchange and redistributes records. That is the moment to inspect skew, shuffle size, partition count, and spill.",
        flow_x + 70,
        flow_y + 70,
        flow_w - 140,
        size=13,
        leading=16,
        color=PALETTE["ink"],
    )

    lower_y = 88
    lower_h = 330
    half_w = (PAGE_W - 2 * margin - gap) / 2
    section(c, margin, lower_y, half_w, lower_h, "Common Healthy Patterns", PALETTE["green"])
    bullet_list(
        c,
        [
            "Read with explicit schemas for production data.",
            "Filter and select early so less data reaches joins and shuffles.",
            "Join with intent: broadcast the small side, repartition when key distribution matters, validate row counts.",
            "Persist only reused expensive intermediates, then materialize once.",
            "Write distributed outputs with sane file sizes, then compact intentionally when needed.",
            "Use EXPLAIN FORMATTED and Spark UI evidence before tuning.",
            "Keep large results distributed; bring only aggregate summaries or bounded samples to the driver.",
            "Reason from partition distribution, not only total row count or total data size.",
            "Tune the query shape first, then memory and executor sizing after evidence.",
            "Prefer simple, checkpointed pipelines when lineage becomes hard to inspect or retry.",
        ],
        margin + 16,
        lower_y + lower_h - 58,
        half_w - 32,
        size=11.1,
    )

    section(c, margin + half_w + gap, lower_y, half_w, lower_h, "Common Anti-Patterns", PALETTE["red"])
    bullet_list(
        c,
        [
            "collect(), toPandas(), or show() on data that is not proven small.",
            "coalesce(1) in production pipelines to force a single output file.",
            "Caching everything without reuse, materialization, or eviction discipline.",
            "Assuming more executors fix skew, bad joins, tiny files, or low task count.",
            "Ignoring Exchange, Sort, BroadcastExchange, and AdaptiveSparkPlan in EXPLAIN.",
            "Treating temp views as durable tables or SQL syntax as proof of cheap execution.",
            "Dropping repartition or cache calls into code without measuring the stage they affect.",
            "Joining before pruning columns or filtering rows that are irrelevant to the result.",
            "Confusing executor memory with driver memory; each process fails independently.",
            "Optimizing for one output file instead of healthy parallel writes and downstream compaction.",
        ],
        margin + half_w + gap + 16,
        lower_y + lower_h - 58,
        half_w - 32,
        size=11.1,
    )

    footer(c, "Poster 1 of 2")
    c.save()


def draw_table(c: canvas.Canvas, x: float, y: float, w: float, h: float, headers: list[str], rows: list[list[str]], widths: list[float]) -> None:
    c.setStrokeColor(PALETTE["line"])
    c.rect(x, y, w, h, stroke=1, fill=0)
    header_h = 26
    c.setFillColor(colors.HexColor("#EAF2F8"))
    c.rect(x, y + h - header_h, w, header_h, stroke=0, fill=1)
    cx = x
    for idx, head in enumerate(headers):
        cw = w * widths[idx]
        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(PALETTE["ink"])
        c.drawString(cx + 6, y + h - 17, head)
        if idx:
            c.setStrokeColor(PALETTE["line"])
            c.line(cx, y, cx, y + h)
        cx += cw
    row_h = (h - header_h) / len(rows)
    for r_idx, row in enumerate(rows):
        ry = y + h - header_h - (r_idx + 1) * row_h
        if r_idx % 2 == 0:
            c.setFillColor(colors.HexColor("#FAFBFC"))
            c.rect(x, ry, w, row_h, stroke=0, fill=1)
        c.setStrokeColor(PALETTE["line"])
        c.line(x, ry, x + w, ry)
        cx = x
        for idx, cell in enumerate(row):
            cw = w * widths[idx]
            draw_wrapped(c, cell, cx + 6, ry + row_h - 14, cw - 12, size=7.6, leading=9.2, max_lines=4)
            cx += cw


def code_block(c: canvas.Canvas, lines: list[str], x: float, y: float, w: float, h: float, title: str) -> None:
    c.setFillColor(colors.HexColor("#1E2933"))
    c.roundRect(x, y, w, h, 8, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#DDE8F2"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + 12, y + h - 17, title)
    c.setFont("Courier", 8.4)
    c.setFillColor(colors.HexColor("#F6FAFD"))
    cy = y + h - 34
    for line in lines:
        c.drawString(x + 12, cy, line)
        cy -= 11


def poster_cheatsheet() -> None:
    path = OUT / "spark_a2_debugging_performance_pyspark_cheatsheet.pdf"
    c = canvas.Canvas(str(path), pagesize=landscape(A2))
    c.setTitle("Spark A2 Debugging, Performance Tuning, and PySpark Cheatsheet")
    c.setFillColor(PALETTE["paper"])
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    header(
        c,
        "Spark Debugging + Performance Cheatsheet",
        "Triage loops, Spark UI evidence, tuning levers, commands, and PySpark snippets",
        "A2 FIELD GUIDE",
    )

    margin = 42
    gap = 18
    top = PAGE_H - 118
    row1_h = 265
    col_w = (PAGE_W - margin * 2 - gap * 2) / 3

    section(c, margin, top - row1_h, col_w, row1_h, "Debugging Triage Loop", PALETTE["blue"])
    bullet_list(
        c,
        [
            "Name the symptom: slow stage, failed task, driver OOM, executor OOM, wrong row count, empty output.",
            "Find the first failing or dominant stage in the Spark UI.",
            "Compare task duration, input size, shuffle read/write, spill, and GC time.",
            "Open EXPLAIN FORMATTED and locate Scan, Filter, Exchange, Join, Aggregate, Sort, Window.",
            "Change one lever, rerun on a representative sample, then compare evidence.",
        ],
        margin + 16,
        top - 58,
        col_w - 32,
        size=11.5,
    )

    section(c, margin + col_w + gap, top - row1_h, col_w, row1_h, "Spark UI Tabs To Read", PALETTE["teal"])
    draw_table(
        c,
        margin + col_w + gap + 14,
        top - row1_h + 20,
        col_w - 28,
        row1_h - 70,
        ["Tab", "Use it for"],
        [
            ["Jobs", "Actions triggered, repeated lineage, failed jobs."],
            ["Stages", "Task counts, skew, shuffle, spill, stragglers."],
            ["SQL", "Physical operators, joins, exchanges, AQE changes."],
            ["Storage", "Cached data size, memory vs disk, replication."],
            ["Executors", "Lost executors, GC, memory, task failures."],
        ],
        [0.25, 0.75],
    )

    section(c, margin + (col_w + gap) * 2, top - row1_h, col_w, row1_h, "Plan Clues", PALETTE["purple"])
    bullet_list(
        c,
        [
            "Exchange: Spark is redistributing data. Expect network, disk, and skew risk.",
            "BroadcastExchange: one side is sent to executors. Great when small; dangerous when mis-sized.",
            "SortMergeJoin: both sides often sorted and shuffled by join key.",
            "HashAggregate: usually partial aggregate before shuffle, final aggregate after shuffle.",
            "AdaptiveSparkPlan: AQE may change joins, coalesce partitions, or handle skew at runtime.",
        ],
        margin + (col_w + gap) * 2 + 16,
        top - 58,
        col_w - 32,
        size=11.3,
    )

    mid_y = 480
    mid_h = 285
    section(c, margin, mid_y, PAGE_W - 2 * margin, mid_h, "Symptom -> Inspect -> Fix", PALETTE["amber"])
    draw_table(
        c,
        margin + 16,
        mid_y + 22,
        PAGE_W - 2 * margin - 32,
        mid_h - 76,
        ["Symptom", "Inspect", "Likely fixes"],
        [
            ["Driver OOM", "collect, toPandas, huge plan, tiny partition metadata, driver logs.", "Keep output distributed, limit/sample, write to storage, simplify lineage, reduce tiny files."],
            ["Executor OOM", "Executor logs, task input, spill, join side size, skewed keys.", "Reduce partition size, fix skew, broadcast only small tables, persist with care, raise memory after evidence."],
            ["One slow task", "Task duration histogram, shuffle read by task, spill, key frequencies.", "Salt hot keys, pre-aggregate, filter invalid heavy keys, enable/tune AQE skew handling."],
            ["Few cores active", "Stage task count, input splits, coalesce/repartition, shuffle partitions.", "Increase partitions, avoid coalesce(1), repartition for balance, compact small files upstream."],
            ["Slow join", "Join strategy, Exchange count, table sizes, null/hot keys.", "Broadcast small side, project/filter first, repartition by key, handle skew, validate join cardinality."],
            ["Repeated work", "Multiple jobs scanning same source or repeating same shuffle.", "Persist reused expensive DataFrames, materialize once, remove unnecessary count/show actions."],
        ],
        [0.22, 0.38, 0.40],
    )

    bottom_y = 88
    bottom_h = 360
    q_w = (PAGE_W - 2 * margin - gap * 3) / 4
    section(c, margin, bottom_y, q_w, bottom_h, "Performance Levers", PALETTE["green"])
    bullet_list(
        c,
        [
            "Partition size: enough tasks for parallelism, not so many that scheduling dominates.",
            "Shuffle partitions: tune `spark.sql.shuffle.partitions`; AQE can coalesce after shuffle.",
            "Join strategy: broadcast small side; avoid shuffling two large skewed inputs blindly.",
            "File layout: compact tiny files; avoid single huge files and many tiny output files.",
            "Cache only reused expensive results; call an action to materialize; unpersist when done.",
            "Push down filters and select columns early.",
        ],
        margin + 16,
        bottom_y + bottom_h - 58,
        q_w - 32,
        size=10.6,
    )

    section(c, margin + q_w + gap, bottom_y, q_w, bottom_h, "Shell + Spark Commands", PALETTE["dark"])
    code_block(
        c,
        [
            "pyspark",
            "spark-submit app.py",
            "spark-submit --master local[*] app.py",
            "spark-submit --conf k=v app.py",
            "spark-submit --packages group:artifact:ver app.py",
            "spark-sql",
            "spark-shell",
            "df.explain('formatted')",
            "spark.catalog.listTables()",
            "spark.catalog.clearCache()",
            "spark.stop()",
            "docker compose up -d",
            "docker compose ps",
            "docker compose logs spark",
            "docker compose exec spark bash",
            "docker compose down",
        ],
        margin + q_w + gap + 16,
        bottom_y + 24,
        q_w - 32,
        bottom_h - 78,
        "common commands",
    )

    section(c, margin + (q_w + gap) * 2, bottom_y, q_w, bottom_h, "PySpark Snippets", PALETTE["blue"])
    code_block(
        c,
        [
            "from pyspark.sql import functions as F",
            "from pyspark.sql.window import Window",
            "df.printSchema()",
            "df.dtypes",
            "df.select('a','b').where(F.col('a') > 0)",
            "df.groupBy('key').agg(F.count('*'), F.avg('x'))",
            "w = Window.partitionBy('key').orderBy(F.desc('x'))",
            "df.withColumn('rn', F.row_number().over(w))",
            "df.join(dim, 'id', 'left')",
            "F.broadcast(dim)",
            "df.repartition(200, 'key')",
            "df.coalesce(20)",
            "df.persist(); df.count()",
            "df.unpersist()",
            "df.write.mode('overwrite').parquet(path)",
            "spark.read.schema(schema).csv(path, header=True)",
        ],
        margin + (q_w + gap) * 2 + 16,
        bottom_y + 24,
        q_w - 32,
        bottom_h - 78,
        "dataframe API",
    )

    section(c, margin + (q_w + gap) * 3, bottom_y, q_w, bottom_h, "Config Quick Refs", PALETTE["red"])
    code_block(
        c,
        [
            "spark.conf.get('spark.sql.shuffle.partitions')",
            "spark.conf.set('spark.sql.shuffle.partitions','200')",
            "spark.conf.set('spark.sql.adaptive.enabled','true')",
            "spark.conf.set('spark.sql.autoBroadcastJoinThreshold','50MB')",
            "spark.conf.set('spark.sql.files.maxPartitionBytes','128MB')",
            "",
            "# inspect shape safely",
            "df.rdd.getNumPartitions()",
            "df.limit(20).show(truncate=False)",
            "df.sample(0.01).count()",
            "df.where(F.col('key').isNull()).count()",
            "df.select('key').groupBy('key').count()",
            "  .orderBy(F.desc('count')).show()",
        ],
        margin + (q_w + gap) * 3 + 16,
        bottom_y + 24,
        q_w - 32,
        bottom_h - 78,
        "configs + checks",
    )

    footer(c, "Poster 2 of 2")
    c.save()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    poster_mental_model()
    poster_cheatsheet()


if __name__ == "__main__":
    main()

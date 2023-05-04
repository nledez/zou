from whoosh import index
from whoosh.query import Or, Term
from whoosh.qparser import MultifieldParser


def create_index(path, schema):
    return index.create_in(path, schema)


def get_index(path):
    return index.open_dir(path)


def index_data(ix, data):
    writer = ix.writer(limitmb=1024)
    writer.add_document(**data)
    writer.commit()
    return writer


def search(ix, query, project_ids=[], limit=10):
    fields = ["name"]
    for field in ix.reader().indexed_field_names():
        if field.startswith("data_") or field == "description":
            fields.append(field)
    query_parser = MultifieldParser(fields, schema=ix.schema)
    whoosh_query = query_parser.parse(query)
    is_project_filter = len(project_ids) > 0
    results = []
    with ix.searcher() as searcher:
        project_id_terms = None
        if is_project_filter:
            project_id_terms = Or(
                [Term("project_id", project_id) for project_id in project_ids]
            )
        search_results = searcher.search(
            whoosh_query, filter=project_id_terms, limit=limit, terms=True
        )
        for result in search_results:
            matched_terms = []
            for matched_term in result.matched_terms():
                matched_terms.append(
                    (matched_term[0], matched_term[1].decode())
                )
            results.append((result["id"], matched_terms))
    return results

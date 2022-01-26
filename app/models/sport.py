from utils.db_delegator import DbDelegator


class Sport:
    table_name = 'sport'
    delegator = DbDelegator(table_name=table_name)

    def __init__(self, name, slug, active) -> None:
        self.name = name
        self.slug = slug
        self.active = active
# services/node_manager.py
from services.neo4j_service import Neo4jService

class NodeManager:
    def create_node(self, name, label, attributes, relations, description, created_by):
        neo4j_service = Neo4jService()
        query = """
        CREATE (n:Node {name: $name, label: $label, attributes: $attributes,
                        relations: $relations, description: $description,
                        created_on: datetime(), modified_on: datetime(),
                        created_by: $created_by})
        RETURN n
        """
        parameters = {
            "name": name,
            "label": label,
            "attributes": attributes,
            "relations": relations,
            "description": description,
            "created_by": created_by
        }
        result = neo4j_service.run_query(query, parameters)
        neo4j_service.close()
        return result

    def retrieve_node(self, name):
        neo4j_service = Neo4jService()
        query = "MATCH (n:Node {name: $name}) RETURN n"
        parameters = {"name": name}
        result = neo4j_service.run_query(query, parameters)
        neo4j_service.close()
        return result

    def update_node(self, name, label=None, attributes=None, relations=None, description=None, modified_by=None):
        neo4j_service = Neo4jService()
        query = """
        MATCH (n:Node {name: $name})
        SET n.label = coalesce($label, n.label),
            n.attributes = coalesce($attributes, n.attributes),
            n.relations = coalesce($relations, n.relations),
            n.description = coalesce($description, n.description),
            n.modified_on = datetime(),
            n.modified_by = $modified_by
        RETURN n
        """
        parameters = {
            "name": name,
            "label": label,
            "attributes": attributes,
            "relations": relations,
            "description": description,
            "modified_by": modified_by
        }
        result = neo4j_service.run_query(query, parameters)
        neo4j_service.close()
        return result

    def delete_node(self, name):
        neo4j_service = Neo4jService()
        query = "MATCH (n:Node {name: $name}) DETACH DELETE n"
        parameters = {"name": name}
        neo4j_service.run_query(query, parameters)
        neo4j_service.close()

    def custom_query(self, query):
        neo4j_service = Neo4jService()
        result = neo4j_service.run_query(query)
        neo4j_service.close()
        return result
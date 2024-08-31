# Project Description: Firelit Tales

**Project Name**: Firelit Tales

**Overview**:  
Firelit Tales is a web application designed to facilitate worldbuilding and storytelling for  
writers, game masters, and creative teams. The platform allows users to create, manage,  
and explore complex worlds, stories, and characters, leveraging the power of Neo4j,  
a graph database, to model intricate relationships and hierarchies within their narratives.

## Key Features:

1. **Flexible Worldbuilding**:  
   - Create nodes representing characters, locations, events, or other elements.  
   - Define attributes like descriptions, timestamps (created, last modified), and authorship.

2. **Graph-Based Data Management**:  
   - Utilize Neo4j's graph database to map out relationships between nodes.  
   - Write and execute Cypher queries directly, enabling deep customization.

3. **Multi-Project Support**:  
   - Organize different worldbuilding projects within a single database using namespaces.  
   - Easily switch between projects while maintaining clear boundaries.

4. **Author and Version Tracking**:  
   - Each node is associated with an author and timestamps for creation and modification.  
   - Ideal for collaborative projects with multiple contributors.

5. **Integrated with Django**:  
   - Backend built on Django, with Neo4j integrated via the official Neo4j Python driver.  
   - Direct interaction with Neo4j without additional ORM layers like Neomodel.

6. **User-Friendly Interface**:  
   - Clean and intuitive interface for efficient project management.  
   - Advanced users can leverage Cypher, while beginners use straightforward forms.

## Target Audience:

- **Writers**: Track complex story elements and their interconnections.  
- **Game Masters**: Manage intricate game worlds, characters, and plots.  
- **Creative Teams**: Collaborate on large-scale projects with relationship tracking.

## Technology Stack:

- **Backend**: Django (Python)  
- **Database**: Neo4j (using the official Neo4j Python driver)  
- **Frontend**: HTML/CSS/JavaScript (Django templates)  
- **IDE**: PyCharm  
- **Development Tools**: Black for formatting, Sonar for code quality.

## Future Enhancements:

- **API Integration**: Expose graph data through RESTful or GraphQL API.  
- **Advanced Visualization**: Implement graph visualization tools.  
- **Collaboration Features**: Add real-time collaboration, role-based access, and version history.

## Conclusion:

Firelit Tales is the ultimate tool for worldbuilding, leveraging Neo4j's graph capabilities  
within the reliable Django framework. Perfect for crafting epic sagas or managing  
tabletop RPG campaigns, Firelit Tales provides the tools you need to bring your world to life.

import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-50))
r=w0.sketch().arc((-63,-98),(48,-51),(42,64)).segment((42,40)).segment((55,24)).segment((63,14)).arc((10,-36),(-48,-84)).segment((-48,-85)).close().assemble().reset().face(w0.sketch().segment((-8,100),(27,80)).arc((11,92),(-8,100)).assemble()).finalize().extrude(100)
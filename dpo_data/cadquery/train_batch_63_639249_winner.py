import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
r=w0.sketch().arc((-93,24),(-77,-24),(-42,16)).arc((-69,14),(-93,24)).assemble().finalize().extrude(-77).union(w0.sketch().segment((39,11),(100,-17)).arc((72,4),(47,22)).arc((43,17),(39,11)).assemble().finalize().extrude(3))
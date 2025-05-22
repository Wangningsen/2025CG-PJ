import cadquery as cq
w0=cq.Workplane('YZ',origin=(-17,0,0))
r=w0.sketch().segment((12,54),(29,54)).arc((22,31),(35,10)).arc((74,-46),(74,23)).arc((76,39),(68,54)).segment((76,54)).segment((76,57)).segment((64,57)).arc((59,60),(54,61)).arc((41,68),(31,57)).segment((12,57)).close().assemble().finalize().extrude(23).union(w0.workplane(offset=35/2).moveTo(-53,-21).cylinder(35,47))
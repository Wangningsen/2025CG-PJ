import cadquery as cq
w0=cq.Workplane('YZ',origin=(46,0,0))
w1=cq.Workplane('XY',origin=(0,0,-68))
r=w0.workplane(offset=-137/2).moveTo(-46.5,-46).box(51,108,137).union(w0.sketch().segment((1,-60),(26,-70)).segment((26,-40)).arc((14,-50),(1,-60)).assemble().finalize().extrude(5)).union(w1.sketch().arc((25,41),(62,30),(92,1)).segment((92,72)).segment((25,72)).close().assemble().finalize().extrude(168))
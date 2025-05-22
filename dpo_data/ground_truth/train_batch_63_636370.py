import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
w1=cq.Workplane('XY',origin=(0,0,-40))
r=w0.sketch().circle(83).circle(55,mode='s').finalize().extrude(141).union(w0.sketch().segment((-64,-54),(64,-54)).segment((64,-17)).arc((18,-5),(64,8)).segment((64,54)).segment((-64,54)).close().assemble().finalize().extrude(144)).union(w1.sketch().segment((-78,-49),(-59,-49)).segment((-59,-38)).arc((-29,-3),(-59,33)).segment((-59,49)).segment((-78,49)).segment((-78,30)).arc((-100,-3),(-78,-36)).close().assemble().finalize().extrude(15))
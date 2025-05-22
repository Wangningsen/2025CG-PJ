import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
w1=cq.Workplane('XY',origin=(0,0,50))
r=w0.workplane(offset=-115/2).moveTo(60,-61.5).box(50,23,115).union(w0.sketch().push([(-55.5,45.5)]).rect(41,55).push([(-55,45)]).rect(40,38,mode='s').finalize().extrude(-75)).union(w0.sketch().arc((-65,69),(-65,22),(-32,55)).arc((-50,59),(-65,69)).assemble().push([(-55,45)]).circle(5,mode='s').finalize().extrude(85)).union(w1.sketch().segment((-15,-82),(25,-82)).arc((63,-40),(8,-54)).segment((-15,-54)).close().assemble().finalize().extrude(-118))
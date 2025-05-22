import cadquery as cq
w0=cq.Workplane('YZ',origin=(-99,0,0))
r=w0.sketch().segment((-5,-90),(-5,-81)).arc((-17,-51),(-5,-22)).segment((-5,-6)).segment((18,-6)).arc((11,44),(47,70)).segment((27,100)).segment((1,72)).arc((-77,-33),(23,-99)).arc((14,-96),(7,-90)).close().assemble().finalize().extrude(22).union(w0.sketch().push([(8,-14)]).circle(4).circle(2,mode='s').finalize().extrude(198))
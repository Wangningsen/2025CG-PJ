import cadquery as cq
w0=cq.Workplane('YZ',origin=(73,0,0))
w1=cq.Workplane('XY',origin=(0,0,8))
r=w0.sketch().arc((-33,-62),(-20,-61),(-19,-73)).arc((28,-64),(36,-16)).arc((16,-16),(18,3)).arc((-33,-9),(-33,-62)).assemble().finalize().extrude(-156).union(w0.sketch().segment((-65,-20),(-20,-20)).segment((-20,-97)).arc((56,0),(-65,-20)).assemble().push([(-7,-79)]).circle(7,mode='s').finalize().extrude(-30)).union(w1.workplane(offset=92/2).moveTo(58,-0.5).box(50,5,92))
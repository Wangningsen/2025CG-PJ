import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
w1=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().push([(-53.5,6.5)]).rect(65,61).rect(35,35,mode='s').finalize().extrude(41).union(w0.sketch().segment((21,-100),(70,-100)).segment((70,-64)).segment((86,-64)).segment((86,-28)).segment((70,-28)).segment((70,12)).segment((21,12)).segment((21,-28)).segment((28,-28)).segment((28,-60)).segment((21,-60)).close().assemble().finalize().extrude(52)).union(w1.sketch().arc((98,-58),(100,-48),(98,-38)).close().assemble().finalize().extrude(29))
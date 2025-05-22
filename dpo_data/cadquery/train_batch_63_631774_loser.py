import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
w1=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().push([(-62,-53)]).circle(39).reset().face(w0.sketch().segment((-61,20),(-55,-12)).segment((-44,-11)).segment((-51,22)).close().assemble()).finalize().extrude(-12).union(w0.sketch().segment((0,6),(29,6)).segment((29,34)).segment((1,34)).segment((1,27)).segment((0,27)).close().assemble().finalize().extrude(5)).union(w1.sketch().arc((81,92),(71,63),(100,76)).arc((85,78),(81,92)).assemble().finalize().extrude(22))
import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
w1=cq.Workplane('YZ',origin=(-41,0,0))
r=w0.sketch().push([(-67,73.5)]).rect(66,45).push([(-98,78)]).circle(1,mode='s').push([(-67,74)]).circle(1,mode='s').finalize().extrude(51).union(w1.sketch().arc((-6,-4),(61,-93),(59,19)).arc((64,38),(61,56)).arc((59,58),(58,61)).arc((47,44),(27,45)).segment((21,45)).segment((21,79)).segment((34,79)).arc((35,81),(37,82)).arc((-25,62),(-6,-4)).assemble().push([(9,22)]).circle(9,mode='s').finalize().extrude(82))
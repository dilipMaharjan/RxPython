import rx
from rx import Observable, Observer

class MyObserver(Observer):
    def on_next(self, x ):
        print("Got: %s" % x )

    def on_error(self,e):
        print("Got error: %e" % e )
    
    def on_completed(self):
        print("Sequence completed.")

xs=Observable.range(1,10)
xs1=Observable.from_("abc")
xs2=xs.merge(xs1).subscribe(print)

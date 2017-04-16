
(defvar a)
(defvar b)
(defvar c)
(defvar d)
(defvar D)
(defvar select)



(write-line " Enter two numbers in : ")

	
	(setf a(read))
	(setf b(read))
	(setq select 1)

        (write-line "enter yr choice ")
        (setf select(read))
        
(case select

	(1 (sb-thread:make-thread(lambda()
				(setf c(+ a b))
				(print "ADDITION in binary: ")
				(format t " ~b" c )
				(print "ADDITION in decimal: ")
				(print c))))

	(2 (sb-thread:make-thread(lambda()
				(setf c(- a b))
				(print "SUBTRACTION in binary: ")1
				(format t " ~b" c )
				(print "SUBTRACTION in decimal: ")
				(print c))))

 	(3 (sb-thread:make-thread(lambda()
				(setf c(* a b))
				(print "MULTIPLICATION in binary: ")
				(format t " ~b" c )
				(print "MULTIPLICATION IN DECIMAL: ")
				(print c))))
	
	(4 (sb-thread:make-thread(lambda()
				(setf c(* a a))
				(print "SQUARE in binary: ")
				(format t " ~b" c )
				(print "SQUARE OF 1st NUMBER  : ")
				(print c))))

	(5 (sb-thread:make-thread(lambda()
				(setf c(* b b b))
				(print "CUBE OF 2ND NUMBER : ")
				(print c))))	


	(6 (sb-thread:make-thread(lambda()
				(setf c(sin a))
				(print "SINE OF 1ST NUMBER : ")
				(print c))))

	(7 (sb-thread:make-thread(lambda()
				(setf c(tan a))
				(print "TAN OF 1ST NUMBER : ")
				(print c))))

	(8 (sb-thread:make-thread(lambda()
				(setf c(cos a))
				(print "COSINE OF 1ST NUMBER : ")
				(print c))))

	(9 (sb-thread:make-thread(lambda()(sleep 0)
				(setf c(min a b))
				(print "MINIMUM NUMBER : ")
				(print c))))

	(10 (sb-thread:make-thread(lambda()
				(setf c(max a b))
				(print "MAXIMUM NUMBER : ")
				(print c)))))

 (exit)      

        

(define (flatmap-not-tail f x)
    (if (null? x) nil
        (append (f (car x)) (flatmap-not-tail f (cdr x)))))

(define (flatmap f x)
    (define (map-rev x m)
        (if (null? x) m
            (map-rev (cdr x) (cons (f (car x)) m))
            )
    )
    (flatrev (map-rev x nil))
)

(define (flatrev x)
    (define (rev-iter x r)
        (if (null? x) r
            (rev-iter (cdr x) (append (car x) r))
        )
    )
    (rev-iter x nil)
)


(define (expand lst)
  (flatmap (lambda (e) (cond ((equal? e 'x) '(x r y f r))
                             ((equal? e 'y) '(l f x l y))
                             (else (list e))
                       )
           ) lst
  )
)

(define (interpret instr dist)
  (flatmap (lambda (e) (cond ((equal? e 'l) (left 90))
                             ((equal? e 'r) (right 90))
                             ((equal? e 'f) (forward dist))
                             (else)
                       )
           ) instr
  )
)

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))
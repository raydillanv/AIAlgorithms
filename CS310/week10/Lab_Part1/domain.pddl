(define (domain strathclyde-taxis)
    (:requirements :strips)
    (:predicates
        (at-taxi ?loc) ; Taxi is at location
        (at-person ?person ?loc) ; Person is at location
        (inside ?person) ; Person is inside the taxi
    )

    ; Move taxi from one location to another
    (:action move
        :parameters (?from ?to)
        :precondition (at-taxi ?from)
        :effect (and
            (not (at-taxi ?from))
            (at-taxi ?to))
    )

    ; Person gets into the taxi
    (:action get-in
        :parameters (?person ?loc)
        :precondition (and
            (at-taxi ?loc)
            (at-person ?person ?loc))
        :effect (and
            (not (at-person ?person ?loc))
            (inside ?person))
    )

    ; Person gets out of the taxi
    (:action get-out
        :parameters (?person ?loc)
        :precondition (and
            (at-taxi ?loc)
            (inside ?person))
        :effect (and
            (not (inside ?person))
            (at-person ?person ?loc))
    )
)
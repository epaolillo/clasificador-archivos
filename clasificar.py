from textar import TextClassifier

tc = TextClassifier(
    texts=[
            "Para hacer una pizza hace falta harina, tomate, queso y jamón",
                    "Para hacer unas empanadas necesitamos tapas de empanadas, tomate, jamón y queso",
                            "Para hacer un daiquiri necesitamos ron, una fruta y un poco de limón",
                                    "Para hacer un cuba libre necesitamos coca, ron y un poco de limón",
                                            "Para hacer una torta de naranja se necesita harina, huevos, leche, ralladura de naranja y polvo de hornear",
                                                    "Para hacer un lemon pie se necesita crema, ralladura de limón, huevos, leche y harina"
                                                        ],
                                                            ids=map(str, range(6))
                                                            )
                                                            
                                                            # entrena un clasificador
                                                            tc.make_classifier(
                                                                name="recetas_classifier",
                                                                    ids=map(str, range(6)),
                                                                        labels=["Comida", "Comida", "Trago", "Trago", "Postre", "Postre"]
                                                                        )
                                                                        
                                                                        labels_considerados, puntajes = tc.classify(
                                                                            classifier_name="recetas_classifier", 
                                                                                examples=[
                                                                                        "Para hacer un bizcochuelo de chocolate se necesita harina, huevos, leche y chocolate negro",
                                                                                                "Para hacer un sanguche de miga necesitamos pan, jamón y queso"
                                                                                                    ]
                                                                                                    )
                                                                                                    
                                                                                                    print labels_considerados
                                                                                                    array(['Comida', 'Postre', 'Trago'], dtype='|S6')
                                                                                                    
                                                                                                    print puntajes
                                                                                                    array([[-3.52493526,  5.85536809, -6.05497008],
                                                                                                           [ 2.801027  , -6.55619473, -3.39598721]])
                                                                                                           
                                                                                                           # el primer ejemplo es un postre
                                                                                                           print sorted(zip(puntajes[0], labels_considerados), reverse=True)
                                                                                                           [(5.8553680868184079, 'Postre'),
                                                                                                            (-3.5249352611212568, 'Comida'),
                                                                                                             (-6.0549700786502845, 'Trago')]
                                                                                                             
                                                                                                             # el segundo ejemplo es una comida
                                                                                                             print sorted(zip(puntajes[1], labels_considerados), reverse=True)
                                                                                                             [(2.8010269985828997, 'Comida'),
                                                                                                              (-3.3959872063363505, 'Trago'),
                                                                                                               (-6.5561947275785393, 'Postre')]

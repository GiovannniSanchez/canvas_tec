$(document).ready(function() {
  // esconder todas las preguntas excepto la primera
  $("#question2,#question3,#question4,#question5").hide();

  // manejar el evento click del botón "Siguiente"
  $(".next-question").click(function() {
    // obtener la pregunta actual
    var currentQuestion = $(this).parent();

    // obtener la siguiente pregunta
    var nextQuestion = currentQuestion.next();

    // esconder la pregunta actual y mostrar la siguiente
    currentQuestion.hide();
    nextQuestion.show();
  });
});

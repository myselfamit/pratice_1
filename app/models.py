from django.db import models

# Create your models here.

"""
There is nothing here
"""

"""

<div class="container1">
    <div class="col">
    <div>
        <canvas id="myChart1"></canvas>
    </div>

    <script>

      const data = {
      labels: [
        'friends',
        'friends you see less',
        'friend requests sent',
        'people who follow you',
        'rejected friend requests',
        'removed friends',
        'who you follow'
      ],
      datasets: [{
        label: 'My First Dataset',
        data: [{{allData1|length}}, {{allData2|length}}, {{allData3|length}}, {{allData4|length}}, {{allData5|length}}, {{allData6|length}}, {{allData7|length}}],
        backgroundColor: [
        "Wheat", "black", "SpringGreen", "MediumPurple", "Gold", "DodgerBlue", "LightCoral"
        ],
        hoverOffset: 4
      }]
    };

    const config = {
      type: 'doughnut',
      data: data,
    };

          const myChart1 = new Chart(
            document.getElementById('myChart1'),
            config
          );


    </script>

    <h3>Total</h3>
    <p style="color:Black">Friends : {{allData1|length}}</p>
    <p style="color:Black">Friends you see less : {{allData2|length}}</p>
    <p style="color:Black">Friend requests sent : {{allData3|length}}</p>
    <p style="color:Black">People who follow you : {{allData4|length}}</p>
    <p style="color:Black">Rejected friend requests : {{allData5|length}}</p>
    <p style="color:Black">Removed friends : {{allData6|length}}</p>
    <p style="color:Black">Who you follow : {{allData7|length}}</p>

</div>
</div>

{% csrf_token %}
<div class="container2">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <div class="col1">
    <div>
        <canvas id="myChart2"></canvas>
    </div>

<script>
  const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
  };

  const config = {
    type: 'bar',
    data: data,
    options: {}
  };
</script>
<script>
  const myChart2 = new Chart(
    document.getElementById('myChart2'),
    config
  );
</script>

</div>
"""
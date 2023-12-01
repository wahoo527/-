$(function () {
    map();
})
function map() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('map_1'));
    // 发送ajax请求
    $.ajax({
        url:'selectMap/',
        dataType:'json',
        type:'post',
        success:function (rs) {
            var option = {
                title: {
                    text: '新冠型肺炎人口来源分析',
                    textStyle: { color: '#fff' },
                    x: 'center'
                },
                tooltip: {
                    trigger: 'item'
                },
                visualMap: {
                    show: false,
                    x: 'left',
                    y: 'bottom',
                    //layoutCenter:['30%','30%'],
                    splitList: [
                        { start: 0, end: 100 },
                        { start: 100, end: 300 },
                        { start: 300, end: 500 },
                        { start: 500, end: 800 },
                        { start: 800, end: 1500 },
                        { start: 1500, end: 6000000 }
                    ],
                    color: ['red', 'yellow', 'Purple', 'DarkCyan', 'green', 'Lime']
                },
                series: [{
                    name: '新冠型肺炎人口来源分析',
                    type: 'map',
                    mapType: 'china',
                    roam: false,
                    label: {
                        normal: {
                            show: true
                        },
                        emphasis: {
                            show: false
                        }
                    },
                    data: rs

                }]
            };
            // 使用刚指定的配置项和数据显示图表
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        },error:function () {
            alert("中国地图服务器报错");
        }
    })

}
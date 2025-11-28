
import { createChart, ColorType, CandlestickSeries, LineSeries } from 'lightweight-charts';
import React, { useEffect, useRef } from 'react';

export const CandleChart = props => {
    const {
        data,
        colors: {
            backgroundColor = 'black',
            lineColor = '#2962FF',
            textColor = 'white',
            areaTopColor = '#2962FF',
            areaBottomColor = 'rgba(41, 98, 255, 0.28)',
        } = {},
    } = props;

    const chartContainerRef = useRef();

    useEffect(
        () => {
            const handleResize = () => {
                chart.applyOptions({ width: chartContainerRef.current.clientWidth });
            };

            const chart = createChart(chartContainerRef.current, {
                layout: {
                    background: { type: ColorType.Solid, color: backgroundColor },
                    textColor,
                },
                width: chartContainerRef.current.clientWidth,
                height: 500,
                grid: {
                    horzLines: {
                        visible: false
                    },
                    vertLines: {
                        visible: false
                    }
                }
            });
            chart.timeScale().fitContent();

            const newSeries = chart.addSeries(CandlestickSeries, { upColor: '#0ECB81',
                downColor: '#F6465D',
                borderDownColor: '#F6465D',
                borderUpColor: '#0ECB81',
                wickDownColor: '#F6465D',
                wickUpColor: '#0ECB81',
                
            });
            
            newSeries.setData(data);

            let lineSeries = chart.addSeries(LineSeries, { color: '#2962FF' });
            //[{time:, high:, low:, close:, open:, ma:}]
            let lineData = data?.map(({ time, ma }) => ({ time, value: ma }));  
            lineSeries.setData(lineData);


            window.addEventListener('resize', handleResize);

            return () => {
                window.removeEventListener('resize', handleResize);

                chart.remove();
            };
        },
        [data, backgroundColor, lineColor, textColor, areaTopColor, areaBottomColor]
    );

    return (
        <div
            ref={chartContainerRef}
        />
    );
};


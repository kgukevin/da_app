export class Weather
{
  day: string;
  temperature: string;
  windspeed: string;
  event: string;

  constructor(day, temperature, windspeed, event) {
    this.day = day;
    this.temperature = temperature;
    this.windspeed = windspeed;
    this.event = event;
  }
}

import Head from "next/head";
import Image from "next/image";
import styles from "@/styles/Home.module.css";
import { log } from "console";
import { GetStaticProps,NextPage } from "next/types";
import Navbar from "@/components/Navbar";
interface Props{
  data:Movie[];
}
interface Movie {
  title: string;
  type:string;
  price:number;
}
const Home:NextPage<Props> = ({data}) => {
  console.log(data[0].price);
  
  return (
    <>
      <Navbar />
    </>
  );
}

export const getStaticProps:GetStaticProps = async (context) => {
  const reponse = await fetch("http://127.0.0.1:8000/auth/movie/");
  const data:Movie[] = await reponse.json();
  return {
    props: {
      data,
    },
  };
}
export default Home;
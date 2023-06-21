import Input from "@/components/input";
import { error, log } from "console";
import React, { useCallback, useState } from "react";
import { useRouter } from "next/router";
const auth = () => {
  
  
  const router = useRouter()
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [password1, setPassword1] = useState("");
  const [password2, setPassword2] = useState("");
  
  const [variant, setVariant] = useState("login");
  const toggleVariant = useCallback(() => {
    setVariant((currentVariant) => (currentVariant == "login" ? "register" : "login"));
  }, []);
  const handleSignUp = async (e:any) => {
    e.preventDefault()
    try {
      if (password1 == password2){
        await signup(name, password1,email)
        router.push('/')
        
      }
      
    } catch (error) {
      console.log(error);
    }
  };
  const handleSignIn = async () => {
    try {
      await signin(email, password1).then(
        resp => {setTimeout(()=>{
          router.push('/')
        },200)}
      );;
      
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="relative h-full w-full bg-[url('https://assets.nflxext.com/ffe/siteui/vlv3/efb4855d-e702-43e5-9997-bba0154152e0/ba1ac8c8-122c-41c8-ace9-4f970749bb89/MM-en-20230417-popsignuptwoweeks-perspective_alpha_website_small.jpg')] bg-no-repeat bg-center bg-fixed object-cover ">
      <div className="bg-black w-full h-full bg-opacity-50">
        <nav className="px-12 py-5 flex justify-between ">
          <div>
            <img src="/images/logo.png" alt="logo" className="h-12" />
          </div>
          <div className="">
            {variant == "register" && (
              <button
                className="bg-red-600 py-3 px-3 text-white rounded-md w-full"
                onClick={toggleVariant}
              >
                Sign In
              </button>
            )}
          </div>
        </nav>
        <div className="flex justify-center">
          <div className="bg-black bg-opacity-70 px-16 self-center">
            <h2 className="text-white text-4xl font-semibold mb-8">
              {variant == "login" ? "Sign In" : "Register"}
            </h2>
            <div className="flex flex-col gap-4 mb-4">
              {variant == "register" && (
                <>
                  <Input
                    label="Username"
                    onChange={(e: any) => setName(e.target.value)}
                    id="name"
                    type="text"
                    value={name}
                  />
                  <Input
                    label="Password"
                    onChange={(e: any) => setPassword1(e.target.value)}
                    id="password1"
                    type="password"
                    value={password1}
                  />
                  <Input
                    label="Re-Password"
                    onChange={(e: any) => setPassword2(e.target.value)}
                    id="password2"
                    type="password"
                    value={password2}
                  />
                </>
              )}

              <Input
                label="Email"
                onChange={(e: any) => setEmail(e.target.value)}
                id="email"
                type="email"
                value={email}
              />
              {variant == 'login' && (
                <Input
                label="Password"
                onChange={(e: any) => setPassword1(e.target.value)}
                id="password1"
                type="password"
                value={password1}
              />
              )}
            </div>
            <button
              className="bg-red-600 py-3 text-white rounded-md w-full"
              onClick={variant == "login" ? handleSignIn : handleSignUp}
            >
              {variant == "login" ? "Login" : "Sign Up"}
            </button>
            {variant == "login" && (
              <p className=" text-neutral-500 mt-12">
                New to NetFlix?
                <span
                  className="text-white ml-1 hover:underline cursor-pointer"
                  onClick={toggleVariant}
                >
                  Sign Up Now
                </span>
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default auth;

const signup = async (username: string, password: string, email: string) => {
  const response = await fetch("http://127.0.0.1:8000/auth/signup/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      "username": username,
      "email": email,
      "password": password,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to sign up");
  }

  return await response.json();
};

const signin = async (email: string, password: string) => {
  const reponse = await fetch("http://127.0.0.1:8000/auth/signin/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });
  if (!reponse.ok) {
    throw new Error("Fail to sign in");
  }
  return await reponse.json();
};
